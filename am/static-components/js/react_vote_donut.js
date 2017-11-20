const { PieChart, Pie, Sector, Cell } = Recharts;

const data = [{name: 'Group A', value: 400}, {name: 'Group B', value: 300},
{name: 'Group C', value: 300}, {name: 'Group D', value: 200}];
const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];
const RADIAN = Math.PI / 180; 

class VoteDonutChart extends React.Component {
    render () {
        return (
            <PieChart width={800} height={600} onMouseEnter={this.onPieEnter}>
                <Pie
                data={data} 
                cx={420} 
                cy={200} 
                startAngle={180}
                endAngle={0}
                innerRadius={40}
                outerRadius={80} 
                fill="#8884d8"
                paddingAngle={5}>
                {
          	        data.map((entry, index) => <Cell fill={COLORS[index % COLORS.length]}/>)
                }
                </Pie>
            </PieChart>
        )
    }
}