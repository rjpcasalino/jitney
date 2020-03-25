'use strict';

const e = React.createElement;

class Widget extends React.Component {
  constructor(props) {
    super(props);
    this.state = { date: new Date(), data: 'Incoming...' };
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
    console.log('Return options');
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

        let darkskyRequest = await fetch(`/forecast?lat=${options.lat}&lng=${options.lng}`, { mode: 'cors' });	
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
ReactDOM.render(e(Widget), domContainer);
