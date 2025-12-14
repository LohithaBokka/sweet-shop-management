import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api";  // backend URL

// Auth APIs
export const registerUser = (data) => axios.post(`${API_URL}/auth/register`, data);
export const loginUser = (data) => axios.post(`${API_URL}/auth/login`, data);

// Sweet APIs
export const getSweets = () => axios.get(`${API_URL}/sweets`);
export const createSweet = (data) => axios.post(`${API_URL}/sweets`, data);
export const updateSweet = (id, data) => axios.put(`${API_URL}/sweets/${id}`, data);
export const deleteSweet = (id) => axios.delete(`${API_URL}/sweets/${id}`);
export const searchSweets = (params) => axios.get(`${API_URL}/sweets/search`, { params });
export const purchaseSweet = (id) => axios.post(`${API_URL}/sweets/${id}/purchase`);
export const restockSweet = (id, quantity=1) => axios.post(`${API_URL}/sweets/${id}/restock`, { quantity });
