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

      if (!!response.minutely) {
        this.setState({
          forecast: response.minutely.summary
        });
      } else {
        this.setState({
          forecast: response.error
        });
      }
    });

    this.state = {
      date: new Date(),
      forecast: 'Fetching...'
    };
  }

  componentDidMount() {
    this.timerID = setInterval(() => this.tick(), 1000);
    this.geoFindMeID = setInterval(() => this.geoFindMe(), 60000);
    this.geoFindMe();
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
    clearInterval(this.getFindMeID);
  }

  tick() {
    this.setState({
      date: new Date()
    });
  }

  render() {
    return e('div', null, null, e('small', null, `${this.state.date.toLocaleTimeString()}`), e('br'), e('small', null, `${this.state.forecast}`));
  }

}

const domContainer = document.querySelector('#morning');
ReactDOM.render(e(Widget), domContainer);