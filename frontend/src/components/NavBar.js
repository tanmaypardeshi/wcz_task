import React, { useState, useEffect } from 'react';
import { useHistory, useLocation } from 'react-router-dom';
import { AppBar, Tab, Tabs } from '@material-ui/core';



const Navbar = () => {
  const history = useHistory();
  const location = useLocation();
  const [value, setValue] = useState(0);

	useEffect(() => {
		const path = location.pathname;
		if(path === '/') {
			setValue(0);
		}
		if(path === '/addteam') {
			setValue(1);
		}
		if(path === '/addmatch') {
			setValue(2);
		}
	}, [location])
	
	const handleChange = (event, newValue) => {
		const tabValue = newValue;
		setValue(tabValue);
		switch(tabValue) {
			case 0:
				history.push('/');
				break;
			case 1:
				history.push('/addteam');
				break;
			case 2:
				history.push('/addmatch');
				break;
			default:
				history.push('/');
				break;
		}
	};

	return (
    <AppBar position="static" style={{height: '3.5em'}}>
      <Tabs
        value={value}
        onChange={handleChange}
        indicatorColor="secondary"
        centered
      >
        <Tab style={{fontSize:'22px'}} label="All Matches" />
        <Tab style={{fontSize:'22px'}} label="Add Team" />
        <Tab style={{fontSize:'22px'}} label="Add Match" />
      </Tabs>
    </AppBar>
  );
}

export default Navbar;