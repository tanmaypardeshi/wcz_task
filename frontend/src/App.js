import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import Navbar from './components/NavBar';
import AllMatches from './components/AllMatches';
import SingleMatch from './components/SingleMatch';
import AddTeam from './components/AddTeam';
import AddMatch from './components/AddMatch'
import { colors } from '@material-ui/core';


const theme = createMuiTheme({
	palette: {
    type: 'dark',
    primary: {
        main: colors.blue[200],
    },
    secondary: {
        main: colors.teal[200],
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <Navbar />
        <Switch>
            <Route exact path='/' component={AllMatches}/>
            <Route path='/match' component={SingleMatch} />
            <Route path='/addteam' component={AddTeam} />
            <Route path='/addmatch' component={AddMatch} /> 
        </Switch>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;
