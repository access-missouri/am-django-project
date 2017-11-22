"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var SiteMenu = function (_React$Component) {
    _inherits(SiteMenu, _React$Component);

    function SiteMenu(props) {
        _classCallCheck(this, SiteMenu);

        var _this = _possibleConstructorReturn(this, (SiteMenu.__proto__ || Object.getPrototypeOf(SiteMenu)).call(this, props));

        _this.state = {
            menuIsOpen: false
        };
        return _this;
    }

    _createClass(SiteMenu, [{
        key: "toggleMenu",
        value: function toggleMenu() {
            this.setState({
                menuIsOpen: !this.state.menuIsOpen
            });
        }
    }, {
        key: "render",
        value: function render() {
            return React.createElement(
                "span",
                null,
                React.createElement(
                    "a",
                    { className: "menu-link", onClick: this.toggleMenu.bind(this) },
                    !this.state.menuIsOpen && React.createElement(
                        "span",
                        null,
                        "Menu"
                    ),
                    this.state.menuIsOpen && React.createElement(
                        "span",
                        null,
                        "Close"
                    )
                ),
                this.state.menuIsOpen && React.createElement("div", { className: "nav-fs-menu" })
            );
        }
    }]);

    return SiteMenu;
}(React.Component);