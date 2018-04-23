class QuickSearchResult extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        return(<li>

        </li>);
    }
}

class AMQuickSearch extends React.Component {

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

        if (this.refs.searchQuery.value){
            toSetQuery['identifier'] = this.refs.searchQuery.value;
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

        this.refs.identifier.value = '';
        this.refs.title.value = '';

        this.componentRefsToQueryState();

        this.setState({
            searchSubmitted: false,
            searchResults: [],
            searchReturned: false
        });

    }

    render () {


        return (
            <div className="reactive-quick-search">
                <form onSubmit={this.submit} className="form" action="" method="get">
                        <div className="form-group">
                            <input type="text"
                                   name="searchQuery"
                                   ref="searchQuery"/>
                        </div>
                        <div className="button-group">
                            <button type="submit" className="button-submit">Search</button>
                            <a className="form-reset link-legislative" onClick={this.resetForm}>Reset</a>
                        </div>
                    </form>
            </div>
        )
    }
}

