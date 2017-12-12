class BillAdvSearchResult extends React.Component {

    constructor(props){
        super(props);
    }

    render() {
        <li>
            <h2><a class="link-legislative" >{this.props.bill_identifier}</a></h2>
            <p class="bill-description">{this.props.bill_title}</p>
            {/*<p class="recent-action">{this.props.} recent actions.</p>*/}
        </li>
    }
}

class BillAdvancedSearch extends React.Component {

    constructor(props){
        super(props);

        this.state =  {
            searchSubmitted: false,
            searchReturned: false,
            searchResults: null,
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

        this.setState(toSetState);

        if (componentWillSearchOnMount){
            this.search();
        }
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

        console.log(this.refs);
    }

    // Actually submit the search as a fetch request to the server
    sendSearch(){

    }



    componentRefsToQueryState(){
        let toSetQuery = {};

        if (this.refs.identifier.value){
            toSetQuery['identifier'] = this.refs.identifier.value;
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

        this.componentRefsToQueryState();
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
                        <div className="button-group">
                            <button type="submit" className="button-submit">Search</button>
                            <a className="form-reset link-legislative" onClick={this.resetForm}>Reset</a>
                        </div>
                    </form>
                </div>


            </div>
        )
    }
}

