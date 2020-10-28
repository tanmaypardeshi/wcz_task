import { Container, TableCell, TableContainer, TableHead, TableBody, TableRow, Paper, Table, Typography } from '@material-ui/core';
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const AllMatches = () => {
    let dummy = null;
    const [matches, setMatches] = useState([]);

    useEffect(() => {
        axios({
            method:'GET',
            headers: {
                "Content-Type": "application/json"
            },
            url: '/getallmatches/'
        })
        .then(response => {
            setMatches(response.data);
        })
        .catch(error => {
            window.alert(error)
        })
    }, [dummy]);
  
    return (
        <Container>
            <Typography variant="h2" style={{
                marginTop:'3%'

            }}>
                Details of All Matches
            </Typography>
            <Typography variant="h5" style={{
                marginTop:'1%'
            }}>
                NOTE: Click on the Match ID to see match details
            </Typography>
            <TableContainer component={Paper} style={{
                marginTop: '2%',
            }}>
                <Table aria-label='simple_table'>
                    <TableHead style={{backgroundColor:'black'}}>
                        <TableRow>
                            <TableCell align="center">Match ID</TableCell>
                            <TableCell align="center">Home Team</TableCell>
                            <TableCell align="center">Away Team</TableCell>
                            <TableCell align="center">Winner Team</TableCell>
                            <TableCell align="center">Win Margin</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {
                            matches.map((match) => {
                                return (
                                    <TableRow key={match.match_id}>
                                        <TableCell align="center">
                                            <Link to={`/match/${match.match_id}`}
                                            style={{
                                                textDecoration:'none',
                                                color:'white'
                                            }}>
                                            {match.match_id}
                                            </Link>
                                        </TableCell>
                                        <TableCell align="center">{match.home_team}</TableCell>
                                        <TableCell align="center">{match.away_team}</TableCell>
                                        <TableCell align="center">{match.winner}</TableCell>
                                        <TableCell align="center">{match.message}</TableCell>
                                    </TableRow>
                                );
                            })
                        }
                    </TableBody>
                </Table>
            </TableContainer>
        </Container>
    )
}

export default AllMatches;