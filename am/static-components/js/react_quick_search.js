function debounce(fn, delay) {
    var timer = null;
    return function () {
        var context = this, args = arguments;
        clearTimeout(timer);
        timer = setTimeout(function () {
            fn.apply(context, args);
        }, delay);
    };
}



class QuickSearchResult extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        return(<div className="result">
            {
                (this.props.result.type === 'bill') &&
                (
                    <span>
                        <h3 className="type-bill">Bill</h3>
                        <h3 className="label"><a href={this.props.result.url}>{this.props.result.identifier} in {this.props.result.session}</a></h3>
                        <p className="description">{this.props.result.description}</p>
                    </span>
                )
            }
            {
                (this.props.result.type === 'person') &&
                (
                    <span>
                        <h3 className="type-person">Person</h3>
                        <h3 className="label"><a href={this.props.result.url}>{this.props.result.name}</a></h3>
                    </span>
                )
            }
            {
                (this.props.result.type === 'finance') &&
                (
                    <span>
                        <h3 className="type-finance">Finance Entity</h3>
                        <h3 className="label"><a href={this.props.result.url}>{this.props.result.name}</a></h3>
                    </span>
                )
            }
        </div>);
    }
}

class AMQuickSearch extends React.Component {

    constructor(props){
        super(props);

        this.state =  {
            searchIsOpen: false,
            searchResults: []
        }

        this.debounceSearch = debounce(this.submitSearch, 1000);
    }

    openSearch(){
        this.setState({
            searchIsOpen: true
        });
    }
    closeSearch(){
        this.setState({
            searchIsOpen: false,
            searchResults: []
        })
    }

    submitSearch(){
        let query = this.refs.searchQuery.value;

        this.setState({
            searchResults:[]
        });


        let billRequestUrl = (`/api/bills/?identifier_search=${encodeURI(query)}`);
        let personRequestUrl = (`/api/people/?index_name_search=${encodeURI(query)}`);
        let financeRequestUrl = (`/api/financeentities/?name_search=${encodeURI(query)}`);



        // Bill Fetch
        fetch(billRequestUrl,{
            headers: {
                "Content-Type": "application/json"
            }
        }).then((response) => {
            let jsonResp = response.json();
            return jsonResp;
        }, function(error) {
            // handle network error
        }).then((data) => {

            let billResults = data['results'].slice(0,4).map(
                function(result){
                    return {
                        type: 'bill',
                        identifier: result.identifier,
                        session: result.legislative_session.name,
                        description: result.title,
                        url: `/bills/${result.id}`
                    }
                }
            );

            this.setState({
                searchResults: this.state.searchResults.concat(billResults),
                searchReturned: true
            });
        });


        // Person Fetch
        fetch(personRequestUrl,{
            headers: {
                "Content-Type": "application/json"
            }
        }).then((response) => {
            let jsonResp = response.json();
            return jsonResp;
        }, function(error) {
            // handle network error
        }).then((data) => {

            let billResults = data['results'].slice(0,4).map(
                function(result){
                    return {
                        type: 'person',
                        name: result.index_name,
                        url: `/people/${result.id}`
                    }
                }
            );

            this.setState({
                searchResults: this.state.searchResults.concat(billResults),
                searchReturned: true
            });
        });

        // Finance Fetch
        fetch(financeRequestUrl,{
            headers: {
                "Content-Type": "application/json"
            }
        }).then((response) => {
            let jsonResp = response.json();
            return jsonResp;
        }, function(error) {
            // handle network error
        }).then((data) => {

            let financeResults = data["results"].slice(0,4).map(
                function(result){
                    return {
                        type: "finance",
                        name: result.name,
                        url: `/finance/entities/${result.id}`
                    }
                }
            );

            this.setState({
                searchResults: this.state.searchResults.concat(financeResults),
                searchReturned: true
            });
        });
    }

    render () {


        return (
            <li className="reactive-quick-search">
                <a href="#" className="search-link" onClick={this.openSearch.bind(this)}>Search</a>
                {
                    this.state.searchIsOpen &&
                    (
                        <div className="quick-search-container">
                            <div className="quick-search-mechanics">
                                <div className="search-window-controls">
                                    <button onClick={this.closeSearch.bind(this)}>Close</button>
                                </div>
                                <div className="search-window-box">
                                    <input type="text"
                                           name="searchQuery"
                                           ref="searchQuery"
                                           onKeyDown={this.debounceSearch.bind(this)}
                                           autoFocus/>
                                </div>
                                {
                                    (this.state.searchResults.length > 0) &&
                                    (
                                        <div className="search-results">
                                            {
                                                this.state.searchResults.map(function(result, i){
                                                    return (
                                                        <QuickSearchResult
                                                            result={result}
                                                        />
                                                    );
                                                })
                                            }
                                        </div>
                                    )
                                }
                            </div>
                        </div>
                    )
                }

            </li>
        )
    }
}

