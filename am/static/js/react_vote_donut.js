'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var _Recharts = Recharts,
    ResponsiveContainer = _Recharts.ResponsiveContainer,
    PieChart = _Recharts.PieChart,
    Pie = _Recharts.Pie,
    Sector = _Recharts.Sector,
    Cell = _Recharts.Cell,
    Tooltip = _Recharts.Tooltip;


var COLORS = ['#436436', '#c51236', '#aaa'];

var VoteDonutChart = function (_React$Component) {
    _inherits(VoteDonutChart, _React$Component);

    function VoteDonutChart() {
        _classCallCheck(this, VoteDonutChart);

        return _possibleConstructorReturn(this, (VoteDonutChart.__proto__ || Object.getPrototypeOf(VoteDonutChart)).apply(this, arguments));
    }

    _createClass(VoteDonutChart, [{
        key: 'render',
        value: function render() {
            return React.createElement(
                ResponsiveContainer,
                { width: "100%", height: 150 },
                React.createElement(
                    PieChart,
                    { onMouseEnter: this.onPieEnter },
                    React.createElement(
                        Pie,
                        {
                            data: [{ name: "Yes", value: this.props.yes }, { name: "No", value: this.props.no }, { name: "Absent/Leave", value: this.props.absent }],
                            cx: "50%",
                            cy: 160,
                            startAngle: 160,
                            endAngle: 20,
                            innerRadius: 80,
                            outerRadius: 120,
                            fill: '#8884d8',
                            paddingAngle: 5
                        },
                        COLORS.map(function (entry, index) {
                            return React.createElement(Cell, { fill: COLORS[index % COLORS.length] });
                        })
                    ),
                    React.createElement(Tooltip, { offset: 5, animationDuration: 200 })
                )
            );
        }
    }]);

    return VoteDonutChart;
}(React.Component);