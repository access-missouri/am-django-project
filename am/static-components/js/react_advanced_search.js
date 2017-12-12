class BillAdvSearchResult extends React.Component {

    constructor(props){
        super(props);
    }

    render() {
        return (<li>
            <h2><a class="link-legislative" href={`/bills/${this.props.bill_id}`}>{this.props.bill_identifier} in {this.props.bill_session_name}</a></h2>
            <p class="bill-description">{this.props.bill_title}</p>
            {/*<p class="recent-action">{this.props.} recent actions.</p>*/}
        </li>);
    }
}

class BillAdvancedSearch extends React.Component {

    constructor(props){
        super(props);

        this.state =  {
            searchSubmitted: false,
            searchReturned: false,
            searchResults: [],
            origin: window.location.origin
        };

        this.search = this.search.bind(this);
        this.parseQuery = this.parseQuery.bind(this);
        this.submit = this.submit.bind(this);
        this.resetForm = this.resetForm.bind(this);
        this.componentRefsToQueryState = this.componentRefsToQueryState.bind(this);
        this.sendSearch = this.sendSearch.bind(this);
    }

    componentDidMount(){
        let queryObj = this.parseQuery(window.location.search.substring(1));

        let componentWillSearchOnMount = false;
        let toSetState = {};

        if (queryObj['page']){
            toSetState['page'] = queryObj['page'];
        }

        if (queryObj['identifier']) {
            this.refs.identifier.value = queryObj['identifier'];
            componentWillSearchOnMount = true;
        }
        if (queryObj['title']) {
            this.refs.title.value = queryObj['title'];
            componentWillSearchOnMount = true;
        }


        this.setState(toSetState);

        if (componentWillSearchOnMount){
            this.search();
        }

        // This code activates history exploration in bills search.
        window.onpopstate = (event) => {
            if (!window.location.search.substring(1)){
                this.resetForm(event);
            }
            else {
                let queryObj = this.parseQuery(window.location.search.substring(1));
                let componentWillSearchOnMount = false;
                if (queryObj['page']){
                    toSetState['page'] = queryObj['page'];
                }

                if (queryObj['identifier']) {
                    this.refs.identifier.value = queryObj['identifier'];
                    componentWillSearchOnMount = true;
                }

                if (queryObj['title']) {
                    this.refs.title.value = queryObj['title'];
                    componentWillSearchOnMount = true;
                }


                this.setState(toSetState);

                if (componentWillSearchOnMount){
                    this.search();
                }
            }
        };
    }


    parseQuery(queryString) {
        let query = {};
        let pairs = (queryString[0] === '?' ? queryString.substr(1) : queryString).split('&');
        for (let i = 0; i < pairs.length; i++) {
            let pair = pairs[i].split('=');
            query[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1] || '');
        }
        return query;
    }

    createSearchQueryString(queryObj){
        let assignArr = [];

        Object.keys(queryObj).forEach(key => {
            assignArr.push(`${key}=${encodeURI(queryObj[key])}`);
        });

        if (assignArr){
            return `?${assignArr.join('&')}`;
        }
        return '';
    }


    // Basic search conduct logic
    search(){
        this.componentRefsToQueryState();

        // This has some serious code smell.
        setTimeout(() => this.sendSearch(), 100);

    }

    // Actually submit the search as a fetch request to the server
    sendSearch(){

        let searchQuery = {};


        if (this.state.page){
            searchQuery['page'] = this.state.page;
        }

        if (this.state.query['identifier']){
            searchQuery['identifier_search'] = this.state.query.identifier;
        }
        if (this.state.query['title']){
            searchQuery['title_search'] = this.state.query.title;
        }

        let requestUrl = (`${this.state.origin}/api/bills/${this.createSearchQueryString(searchQuery)}`);

        fetch(requestUrl,{
            headers: {
                "Content-Type": "application/json"
            }
        }).then((response) => {
            let jsonResp = response.json();
            return jsonResp;
        }, function(error) {
            // handle network error
        }).then((data) => {

            this.setState({
                searchResults: data['results'],
                searchReturned: true
            });
            history.pushState(this.state.query,
                "Bill Search Results - Access Missouri",
                `/search/bills/${this.createSearchQueryString(this.state.query)}`);
        });

    }



    componentRefsToQueryState(){
        let toSetQuery = {};

        if (this.refs.identifier.value){
            toSetQuery['identifier'] = this.refs.identifier.value;
        }
        if (this.refs.title.value){
            toSetQuery['title'] = this.refs.title.value;
        }

        this.setState({
            query : toSetQuery
        });
    }

    submit(e){
        e.preventDefault();
        this.search();
    }

    resetForm(e){
        e.preventDefault();

        this.refs.identifier.value = '';
        this.refs.title.value = '';

        this.componentRefsToQueryState();

        this.setState({
            searchSubmitted: false,
            searchResults: [],
            searchReturned: false
        });

        history.pushState({},
            "Bill Search - Access Missouri",
            `/search/bills/`);
    }

    render () {


        return (
            <div className="bill-advanced-search">
                <div className="full-cluster search-fields">
                    <form onSubmit={this.submit} className="form" action="" method="get">
                        <div className="form-group">
                            <label htmlFor="name">Bill Identifier: </label>
                            <input type="text"
                                   name="identifier"
                                   ref="identifier"/>
                        </div>
                        <div className="form-group">
                            <label htmlFor="title">Bill Description: </label>
                            <input type="text"
                                   name="title"
                                   ref="title"/>
                        </div>
                        <div className="button-group">
                            <button type="submit" className="button-submit">Search</button>
                            <a className="form-reset link-legislative" onClick={this.resetForm}>Reset</a>
                        </div>
                    </form>
                </div>

                {this.state.searchReturned && this.state.searchResults &&

                <div className="full-cluster search-results">
                    <ul className="search-results bill-search-results">
                        {
                            this.state.searchResults.map(function(result, i){
                                return (
                                    <BillAdvSearchResult
                                        bill_identifier={result.identifier}
                                        bill_title={result.title}
                                        bill_session_name={result.legislative_session.name}
                                        bill_id={result.id}
                                    />
                                );
                            })
                        }
                    </ul>
                </div>

                }

            </div>
        )
    }
}

