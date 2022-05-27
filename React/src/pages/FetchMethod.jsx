import React, { useState, useEffect } from 'react';
import axios from 'axios';

// create a hero state variable.

/*
    use useEffect hook and axios to fetch json data in django_rest.
*/

function FetchMethod() {
  const [heroes, setHeroes] = useState([]);

  useEffect(() => {
      axios.get("http://127.0.0.1:8000/?format=json")
        .then(response => {
            console.log(response)
            setHeroes(response.data)
        })
        .catch(err => {
            console.log(err)
        })
  }, []);

  return (
    <div>
        <h1>My Heroes :</h1>
        <ul>
            {
                heroes.map(hero => (
                    <li key={hero.name}>{hero.alias}</li>
                ))
            }
        </ul>
    </div>
  )
}

export default FetchMethod;