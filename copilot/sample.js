// create react component that get a number and multiply it by 2
// import useState
import { useState } from 'react';
function Multiply(props){
    const [value, setValue] = useState(1);
    return (
        <div>
            <input type="number" value={value} onChange={e => setValue(e.target.value)} />
            <button onClick={() => setValue(value * 2)}>Multiply</button>
        </div>
    );
    

}