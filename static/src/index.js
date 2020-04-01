'use strict';

const e = React.createElement;

class Widget extends React.Component {
  constructor(props) {
    super(props);
    this.state = { date: new Date(), forecastName: 'Fetching...', forecast: '', temp: '', windSpeed: '', windDir: '' };
  }

  componentDidMount() {
	this.timerID = setInterval(
		() => this.tick(),
		1000
	);
	this.geoFindMeID = setInterval(
		() => this.geoFindMe(),
		60000
	);
	this.geoFindMe();
  }

  componentWillUnmount() {
	  clearInterval(this.timerID);
	  clearInterval(this.getFindMeID);
  }

tick() {
	this.setState({date: new Date()});
}

geoFindMe = async () => {
  
 const success = (position) => {
   let options = {
	lat: null,
	lng: null
    };
    options.lat  = position.coords.latitude;
    options.lng = position.coords.longitude;
    this.fetchForecast(options);
  }

  const error = () => {
    console.log('Unable to retrieve your location');
    this.setState({ forecast: 'Unable to fetch forecast!' })
  }

  if (!navigator.geolocation) {
    console.log('Geolocation is not supported by your browser');
    this.setState({ forecast: 'Geolocation not supported!' })
  } else {
    navigator.geolocation.getCurrentPosition(success, error);
  }
}


fetchForecast = async (options) => { 
        let request = await fetch(`/forecast?lat=${options.lat}&lng=${options.lng}`, { mode: 'cors' });	
	let response = await request.json();
	console.log(response);
	if (!!response) {
		this.setState({ forecast: response.shortForecast, temp: response.temperature, windSpeed: response.windSpeed, windDir: response.windDirection});
	} else {
		this.setState({ forecast: response.error });
	}
}


  render() {
	  return e('div', null, null,
	  	  e('small', null, `${this.state.date.toLocaleTimeString()}`), 
		  e('br'), 
		  e('small', null, `${this.state.forecastName}`),
		  e('br'), 
		  e('small', null, `${this.state.forecast}`),
		  e('br'), 
		  e('small', null, `${this.state.temp} F`),
		  e('br'), 
		  e('small', null, `${this.state.windSpeed} ${this.state.windDir}`),
	  );
  }
}

const domContainer = document.querySelector('#morning');
ReactDOM.render(e(Widget), domContainer);
