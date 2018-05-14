class EntityAdvSearchResult extends React.Component {

    constructor(props){
        super(props);
    }

    render() {
        return (<li>
            <h2><a class="link-finance" href={`/finance/entities/${this.props.person_id}`}>{this.props.name}</a></h2>
            {/*<p class="bill-description">{this.props.bill_title}</p>*/}
            {/*<p class="recent-action">{this.props.} recent actions.</p>*/}
        </li>);
    }
}

class FinanceAdvancedSearch extends React.Component {

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

        if (queryObj['name']) {
            this.refs.p_name.value = queryObj['name'];
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

                if (queryObj['name']) {
                    this.refs.p_name.value = queryObj['name'];
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

        if (this.state.query['name']){
            searchQuery['name_search'] = this.state.query.name;
        }

        let requestUrl = (`${this.state.origin}/api/financeentities/${this.createSearchQueryString(searchQuery)}`);

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
                "Finance Search Results - Access Missouri",
                `/search/finance/${this.createSearchQueryString(this.state.query)}`);
        });

    }



    componentRefsToQueryState(){
        let toSetQuery = {};

        if (this.refs.p_name.value){
            toSetQuery['name'] = this.refs.p_name.value;
        }

        this.setState({
            query : toSetQuery
        });
    }

    submit(e){
        e.preventDefault();
        this.setState({
            searchSubmitted: true
        });
        this.search();
    }

    resetForm(e){
        e.preventDefault();

        this.refs.p_name.value = '';

        this.componentRefsToQueryState();

        this.setState({
            searchSubmitted: false,
            searchResults: [],
            searchReturned: false
        });

        history.pushState({},
            "Finance Search - Access Missouri",
            `/search/finance/`);
    }

    render () {


        return (
            <div className="bill-advanced-search">
                <div className="full-cluster search-fields">
                    <form onSubmit={this.submit} className="form" action="" method="get">
                        <div className="form-group">
                            <label htmlFor="name">Name: </label>
                            <input type="text"
                                   name="p_name"
                                   ref="p_name"/>
                        </div>
                        <div className="button-group">
                            <button type="submit" className="button-submit">Search</button>
                            <a className="form-reset link-people" onClick={this.resetForm}>Reset</a>
                        </div>
                    </form>
                </div>

                {this.state.searchReturned && this.state.searchResults &&

                <div className="full-cluster search-results">
                    <ul className="search-results bill-search-results">
                        {
                            this.state.searchResults.map(function(result, i){
                                return (
                                    <EntityAdvSearchResult
                                        name={result.name}
                                        entity_id={result.id}
                                    />
                                );
                            })
                        }
                    </ul>
                </div>

                }

                {
                    this.state.searchSubmitted && !this.state.searchReturned &&
                    <div className="loader">Loading...</div>
                }

                {
                    this.state.searchReturned &&
                    (this.state.searchResults.length < 1) &&
                    <div className="no-results">
                        <span>:(</span>
                        <h3>It looks like we can't find that.</h3>
                        <p>Sometimes this can happen. You may want to try a search with fewer options.</p>
                    </div>

                }

            </div>
        )
    }
}

