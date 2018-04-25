const { Map:LeafletMap, TileLayer, Marker, Popup } = window.ReactLeaflet;

class DistrictMap extends React.Component {

    render() {
        // const position = [this.props.bbox_top_lat, this.props.bbox_left_lon];
        const position = [
            (this.props.bbox_left_lon+this.props.bbox_right_lon)/2,
            (this.props.bbox_top_lat+this.props.bbox_bottom_lat)/2
            ];
        return (<div className="map-contain">
            <LeafletMap center={position} zoom={9}>
                <TileLayer
                            url='https://api.mapbox.com/styles/v1/nathanlawrence/cj7dsc9j815p02spkufl6xrdt/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoibmF0aGFubGF3cmVuY2UiLCJhIjoiY2l5dzl5NDA4MDAxeTJxcWU3NTVwaHBsMyJ9.kNUj23zWfRJNLl2W8hsAyA'
                        />
            </LeafletMap>
            </div>
        )
    }
}