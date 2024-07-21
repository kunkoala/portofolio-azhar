const API_URL = process.env.API_URL;

const callApi = async (query: string) => {
  const url = `${API_URL}${query}`;
  const response = await fetch(url, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error(response.statusText);
  }

  return response.json();
};

export const getByQuery = async (query: string) => {
  const response = await callApi(query);
  return response;
};
