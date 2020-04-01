'use strict';

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

const e = React.createElement;

class Widget extends React.Component {
  constructor(props) {
    super(props);

    _defineProperty(this, "geoFindMe", async () => {
      const success = position => {
        let options = {
          lat: null,
          lng: null
        };
        options.lat = position.coords.latitude;
        options.lng = position.coords.longitude;
        this.fetchForecast(options);
      };

      const error = () => {
        console.log('Unable to retrieve your location');
        this.setState({
          forecast: 'Unable to fetch forecast!'
        });
      };

      if (!navigator.geolocation) {
        console.log('Geolocation is not supported by your browser');
        this.setState({
          forecast: 'Geolocation not supported!'
        });
      } else {
        navigator.geolocation.getCurrentPosition(success, error);
      }
    });

    _defineProperty(this, "fetchForecast", async options => {
      let request = await fetch(`/forecast?lat=${options.lat}&lng=${options.lng}`, {
        mode: 'cors'
      });
      let response = await request.json();
      console.log(response);

      if (!!response) {
        this.setState({
          forecast: response
        });
      } else {
        this.setState({
          forecast: response.error
        });
      }
    });

    this.state = {
      forecast: ''
    };
  }

  componentDidMount() {
    this.geoFindMeID = setInterval(() => this.geoFindMe(), 60000);
    this.geoFindMe();
  }

  componentWillUnmount() {
    clearInterval(this.getFindMeID);
  }

  render() {
    if (this.state.forecast.name != undefined) {
      return e('div', null, null, e('br'), e('small', null, `${this.state.forecast.name}`), e('br'), e('small', null, `${this.state.forecast.shortForecast}`), e('br'), e('small', null, `${this.state.forecast.temperature}`), e('small', null, `${this.state.forecast.temperatureUnit}`), e('br'), e('small', null, `${this.state.forecast.windSpeed} ${this.state.forecast.windDirection}`), e('br'), e('img', {
        src: this.state.forecast.icon,
        id: 'weather-api-icon'
      }));
    }

    return null;
  }

}

const domContainer = document.querySelector('#morning');
ReactDOM.render(e(Widget), domContainer);