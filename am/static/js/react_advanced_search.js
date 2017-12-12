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
            React.createElement(
                "li",
                null,
                React.createElement(
                    "h2",
                    null,
                    React.createElement(
                        "a",
                        { "class": "link-legislative" },
                        this.props.bill_identifier
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
            searchResults: null
        };

        _this2.search = _this2.search.bind(_this2);
        _this2.parseQuery = _this2.parseQuery.bind(_this2);
        _this2.submit = _this2.submit.bind(_this2);
        _this2.resetForm = _this2.resetForm.bind(_this2);
        _this2.componentRefsToQueryState = _this2.componentRefsToQueryState.bind(_this2);
        return _this2;
    }

    _createClass(BillAdvancedSearch, [{
        key: "componentDidMount",
        value: function componentDidMount() {
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

            this.setState(toSetState);

            if (componentWillSearchOnMount) {
                this.search();
            }
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
        key: "search",
        value: function search() {
            this.componentRefsToQueryState();

            console.log(this.refs);
        }
    }, {
        key: "componentRefsToQueryState",
        value: function componentRefsToQueryState() {
            var toSetQuery = {};

            if (this.refs.identifier.value) {
                toSetQuery['identifier'] = this.refs.identifier.value;
            }

            this.setState({
                query: toSetQuery
            });
        }
    }, {
        key: "submit",
        value: function submit(e) {
            e.preventDefault();
            this.search();
        }
    }, {
        key: "resetForm",
        value: function resetForm(e) {
            e.preventDefault();

            this.refs.identifier.value = '';

            this.componentRefsToQueryState();
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
                )
            );
        }
    }]);

    return BillAdvancedSearch;
}(React.Component);