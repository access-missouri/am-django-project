class SiteMenu extends React.Component {

    constructor(props){
        super(props);

        this.state =  {
                menuIsOpen: false
            }
    }

    toggleMenu(){
        this.setState({
            menuIsOpen: !this.state.menuIsOpen
        })
    }


    render () {
        return (
            <span>
                <a className="menu-link" onClick={this.toggleMenu.bind(this)}>{ !this.state.menuIsOpen && <span>Menu</span> }{ this.state.menuIsOpen && <span>Close</span>}</a>
                {
                    this.state.menuIsOpen &&
                        <div className={"nav-fs-menu"}>

                        </div>
                }
            </span>
        )
    }
}