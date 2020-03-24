'use strict';

const e = React.createElement;

class Morning extends React.Component {
  constructor(props) {
    super(props);
    this.state = { date: new Date(), data: 'Incoming...' };
  }

  componentDidMount() {
	this.timerID = setInterval(
		() => this.tick(),
		1000
	);
	this.weatherID = setInterval(
		() => this.fetchWeather(),
		600000
	);
	this.fetchWeather();
  }

  componentWillUnmount() {
	  clearInterval(this.timerID);
	  clearInterval(this.weatherID);
  }

tick() {
	this.setState({date: new Date()});
}

fetchWeather = async () => { 
	let options = {
		lat: null,
		lng: null
	};

	let res = await fetch('https://location.services.mozilla.com/v1/geolocate?key=test', { mode: 'cors' });
	let resJSON = await res.json();

	options.lat = resJSON.location.lat;
	options.lng = resJSON.location.lng;

        let darkskyRequest = await fetch(`/morning?lat=${options.lat}&lng=${options.lng}`, { mode: 'cors' });	
	let darkskyResponse = await darkskyRequest.json();
	
	this.setState({ data: darkskyResponse.minutely.summary });
}


  render() {
	  return e('div', null, null,
	  	  e('small', null, `${this.state.date.toLocaleTimeString()}`), 
		  e('br'), 
		  e('small', null, `${this.state.data}`),
	  );
  }
}

const domContainer = document.querySelector('#morning');
ReactDOM.render(e(Morning), domContainer);
