const {ResponsiveContainer, PieChart, Pie, Sector, Cell, Tooltip} = Recharts;

const COLORS = ["#436436", "#c51236", "#aaa"];

class VoteDonutChart extends React.Component {
    render() {
        return (
            <ResponsiveContainer width={"100%"} height={150}>
                <PieChart onMouseEnter={this.onPieEnter}>
                    <Pie
                        data={[
                            {name: "Yes", value: this.props.yes},
                            {name: "No", value: this.props.no},
                            {name: "Absent/Leave", value: this.props.absent}]}
                        cx={"50%"}
                        cy={160}
                        startAngle={160}
                        endAngle={20}
                        innerRadius={80}
                        outerRadius={120}
                        fill="#8884d8"
                        paddingAngle={5}
                    >
                        {
                            COLORS.map((entry, index) => <Cell fill={COLORS[index % COLORS.length]}/>)
                        }
                    </Pie>
                    <Tooltip offset={5} animationDuration={200}/>
                </PieChart>
            </ResponsiveContainer>
        )
    }
}