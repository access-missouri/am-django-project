"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var BillAdvSearchResult = function (_React$Component) {
    _inherits(BillAdvSearchResult, _React$Component);

    function BillAdvSearchResult(props) {
        _classCallCheck(this, BillAdvSearchResult);

        return _possibleConstructorReturn(this, (BillAdvSearchResult.__proto__ || Object.getPrototypeOf(BillAdvSearchResult)).call(this, props));
    }

    _createClass(BillAdvSearchResult, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "li",
                null,
                React.createElement(
                    "h2",
                    null,
                    React.createElement(
                        "a",
                        { "class": "link-legislative", href: "/bills/" + this.props.bill_id },
                        this.props.bill_identifier,
                        " in ",
                        this.props.bill_session_name
                    )
                ),
                React.createElement(
                    "p",
                    { "class": "bill-description" },
                    this.props.bill_title
                )
            );
        }
    }]);

    return BillAdvSearchResult;
}(React.Component);

var BillAdvancedSearch = function (_React$Component2) {
    _inherits(BillAdvancedSearch, _React$Component2);

    function BillAdvancedSearch(props) {
        _classCallCheck(this, BillAdvancedSearch);

        var _this2 = _possibleConstructorReturn(this, (BillAdvancedSearch.__proto__ || Object.getPrototypeOf(BillAdvancedSearch)).call(this, props));

        _this2.state = {
            searchSubmitted: false,
            searchReturned: false,
            searchResults: [],
            origin: window.location.origin
        };

        _this2.search = _this2.search.bind(_this2);
        _this2.parseQuery = _this2.parseQuery.bind(_this2);
        _this2.submit = _this2.submit.bind(_this2);
        _this2.resetForm = _this2.resetForm.bind(_this2);
        _this2.componentRefsToQueryState = _this2.componentRefsToQueryState.bind(_this2);
        _this2.sendSearch = _this2.sendSearch.bind(_this2);
        return _this2;
    }

    _createClass(BillAdvancedSearch, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            var _this3 = this;

            var queryObj = this.parseQuery(window.location.search.substring(1));

            var componentWillSearchOnMount = false;
            var toSetState = {};

            if (queryObj['page']) {
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

            if (componentWillSearchOnMount) {
                this.search();
            }

            // This code activates history exploration in bills search.
            window.onpopstate = function (event) {
                if (!window.location.search.substring(1)) {
                    _this3.resetForm(event);
                } else {
                    var _queryObj = _this3.parseQuery(window.location.search.substring(1));
                    var _componentWillSearchOnMount = false;
                    if (_queryObj['page']) {
                        toSetState['page'] = _queryObj['page'];
                    }

                    if (_queryObj['identifier']) {
                        _this3.refs.identifier.value = _queryObj['identifier'];
                        _componentWillSearchOnMount = true;
                    }

                    if (_queryObj['title']) {
                        _this3.refs.title.value = _queryObj['title'];
                        _componentWillSearchOnMount = true;
                    }

                    _this3.setState(toSetState);

                    if (_componentWillSearchOnMount) {
                        _this3.search();
                    }
                }
            };
        }
    }, {
        key: "parseQuery",
        value: function parseQuery(queryString) {
            var query = {};
            var pairs = (queryString[0] === '?' ? queryString.substr(1) : queryString).split('&');
            for (var i = 0; i < pairs.length; i++) {
                var pair = pairs[i].split('=');
                query[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1] || '');
            }
            return query;
        }
    }, {
        key: "createSearchQueryString",
        value: function createSearchQueryString(queryObj) {
            var assignArr = [];

            Object.keys(queryObj).forEach(function (key) {
                assignArr.push(key + "=" + encodeURI(queryObj[key]));
            });

            if (assignArr) {
                return "?" + assignArr.join('&');
            }
            return '';
        }

        // Basic search conduct logic

    }, {
        key: "search",
        value: function search() {
            var _this4 = this;

            this.componentRefsToQueryState();

            // This has some serious code smell.
            setTimeout(function () {
                return _this4.sendSearch();
            }, 100);
        }

        // Actually submit the search as a fetch request to the server

    }, {
        key: "sendSearch",
        value: function sendSearch() {
            var _this5 = this;

            var searchQuery = {};

            if (this.state.page) {
                searchQuery['page'] = this.state.page;
            }

            if (this.state.query['identifier']) {
                searchQuery['identifier_search'] = this.state.query.identifier;
            }
            if (this.state.query['title']) {
                searchQuery['title_search'] = this.state.query.title;
            }

            var requestUrl = this.state.origin + "/api/bills/" + this.createSearchQueryString(searchQuery);

            fetch(requestUrl, {
                headers: {
                    "Content-Type": "application/json"
                }
            }).then(function (response) {
                var jsonResp = response.json();
                return jsonResp;
            }, function (error) {
                // handle network error
            }).then(function (data) {

                _this5.setState({
                    searchResults: data['results'],
                    searchReturned: true
                });
                history.pushState(_this5.state.query, "Bill Search Results - Access Missouri", "/search/bills/" + _this5.createSearchQueryString(_this5.state.query));
            });
        }
    }, {
        key: "componentRefsToQueryState",
        value: function componentRefsToQueryState() {
            var toSetQuery = {};

            if (this.refs.identifier.value) {
                toSetQuery['identifier'] = this.refs.identifier.value;
            }
            if (this.refs.title.value) {
                toSetQuery['title'] = this.refs.title.value;
            }

            this.setState({
                query: toSetQuery
            });
        }
    }, {
        key: "submit",
        value: function submit(e) {
            e.preventDefault();
            this.setState({
                searchSubmitted: true
            });
            this.search();
        }
    }, {
        key: "resetForm",
        value: function resetForm(e) {
            e.preventDefault();

            this.refs.identifier.value = '';
            this.refs.title.value = '';

            this.componentRefsToQueryState();

            this.setState({
                searchSubmitted: false,
                searchResults: [],
                searchReturned: false
            });

            history.pushState({}, "Bill Search - Access Missouri", "/search/bills/");
        }
    }, {
        key: "render",
        value: function render() {

            return React.createElement(
                "div",
                { className: "bill-advanced-search" },
                React.createElement(
                    "div",
                    { className: "full-cluster search-fields" },
                    React.createElement(
                        "form",
                        { onSubmit: this.submit, className: "form", action: "", method: "get" },
                        React.createElement(
                            "div",
                            { className: "form-group" },
                            React.createElement(
                                "label",
                                { htmlFor: "name" },
                                "Bill Identifier: "
                            ),
                            React.createElement("input", { type: "text",
                                name: "identifier",
                                ref: "identifier" })
                        ),
                        React.createElement(
                            "div",
                            { className: "form-group" },
                            React.createElement(
                                "label",
                                { htmlFor: "title" },
                                "Bill Description: "
                            ),
                            React.createElement("input", { type: "text",
                                name: "title",
                                ref: "title" })
                        ),
                        React.createElement(
                            "div",
                            { className: "button-group" },
                            React.createElement(
                                "button",
                                { type: "submit", className: "button-submit" },
                                "Search"
                            ),
                            React.createElement(
                                "a",
                                { className: "form-reset link-legislative", onClick: this.resetForm },
                                "Reset"
                            )
                        )
                    )
                ),
                this.state.searchReturned && this.state.searchResults && React.createElement(
                    "div",
                    { className: "full-cluster search-results" },
                    React.createElement(
                        "ul",
                        { className: "search-results bill-search-results" },
                        this.state.searchResults.map(function (result, i) {
                            return React.createElement(BillAdvSearchResult, {
                                bill_identifier: result.identifier,
                                bill_title: result.title,
                                bill_session_name: result.legislative_session.name,
                                bill_id: result.id
                            });
                        })
                    )
                ),
                this.state.searchSubmitted && !this.state.searchReturned && React.createElement(
                    "div",
                    { className: "loader" },
                    "Loading..."
                ),
                this.state.searchReturned && this.state.searchResults.length < 1 && React.createElement(
                    "div",
                    { className: "no-results" },
                    React.createElement(
                        "span",
                        null,
                        ":("
                    ),
                    React.createElement(
                        "h3",
                        null,
                        "It looks like we can't find that."
                    ),
                    React.createElement(
                        "p",
                        null,
                        "Sometimes this can happen. You may want to try a search with fewer options."
                    )
                )
            );
        }
    }]);

    return BillAdvancedSearch;
}(React.Component);