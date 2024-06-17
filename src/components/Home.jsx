import React, { useState } from 'react';
import axios from 'axios';
import './Home.css';

export default function Home() {
  const [formData, setFormData] = useState({
    Name: '',
    Age: '',
    Email: '',
    Company: '',
    Amount: '',
    Hospital: '',
    County: '',
  });

  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [id]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/submit', formData);
      console.log('Data submitted successfully:', response.data);
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  return (
    <div>
      <div className='container'>
        <form className="row g-3" id='form' onSubmit={handleSubmit}>
          <div className="col-md-7">
            <label htmlFor="Name" className="form-label">Name:</label>
            <input type="text" className="form-control" id="Name" value={formData.Name} onChange={handleChange} />
          </div>
          <div className="col-md-3">
            <label htmlFor="Age" className="form-label">Age:</label>
            <input type="number" className="form-control" id="Age" value={formData.Age} onChange={handleChange} />
          </div>
          <div className="col-10">
            <label htmlFor="Email" className="form-label">Email:</label>
            <input type="email" className="form-control" id="Email" value={formData.Email} onChange={handleChange} />
          </div>
          <div className="col-md-5">
            <label htmlFor="Company" className="form-label">Insurance Company:</label>
            <input type="text" className="form-control" id="Company" value={formData.Company} onChange={handleChange} />
          </div>
          <div className="col-md-5">
            <label htmlFor="Amount" className="form-label">Amount spent:</label>
            <input type="number" className="form-control" id="Amount" value={formData.Amount} onChange={handleChange} />
          </div>
          <div className="col-md-5">
            <label htmlFor="Hospital" className="form-label">Hospital:</label>
            <input type="text" className="form-control" id="Hospital" value={formData.Hospital} onChange={handleChange} />
          </div>
          <div className="col-md-5">
            <label htmlFor="County" className="form-label">County:</label>
            <input type="text" className="form-control" id="County" value={formData.County} onChange={handleChange} />
          </div>
          <div className="col-12">
            <button type="submit" className="btn btn-primary">Submit</button>
          </div>
        </form>
      </div>
    </div>
  );
}


