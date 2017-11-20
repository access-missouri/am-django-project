const { PieChart, Pie, Sector, Cell } = Recharts;

const COLORS = ['#436436', '#c51236', '#aaa'];

class VoteDonutChart extends React.Component {
    render () {
        return (
            <PieChart width={800} height={600} onMouseEnter={this.onPieEnter}>
                <Pie
                data={[
                    {name: "Yes", value: this.props.yes},
                    {name: "No", value: this.props.no},
                    {name: "Absent/Leave", value: this.props.absent}]} 
                cx={420} 
                cy={200} 
                startAngle={180}
                endAngle={0}
                innerRadius={40}
                outerRadius={80} 
                fill="#8884d8"
                paddingAngle={5}>
                {
          	        COLORS.map((entry, index) => <Cell fill={COLORS[index % COLORS.length]}/>)
                }
                </Pie>
            </PieChart>
        )
    }
}