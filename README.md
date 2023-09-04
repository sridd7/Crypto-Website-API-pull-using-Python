# Crypto Data Retrieval and Visualization

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Server Setup](#server-setup)
- [Connecting to Power BI](#connecting-to-power-bi)
- [User Interface (Optional)](#user-interface-optional)
- [Documentation and Maintenance](#documentation-and-maintenance)
- [Contributing](#contributing)
- [License](#license)
- [Testing the API Endpoint with Postman](#testing-the-api-endpoint-with-postman) <!-- New section -->

---

## Overview

The Crypto Data Retrieval and Visualization project is designed to fetch real-time cryptocurrency data from the CoinMarketCap API, store it on a server, and connect it to a powerful visualization tool like Power BI. This comprehensive solution enables you to analyze cryptocurrency trends, track prices, and gain insights for informed investment decisions.

### Features

- **Data Retrieval**: Fetch real-time cryptocurrency data for up to 5000 cryptocurrencies and convert values to Indian Rupees (INR) using the CoinMarketCap API.

- **Server Storage**: Store cryptocurrency data on a server, allowing for historical data retrieval and analysis.

- **Power BI Integration**: Connect the server to Power BI for creating interactive and customizable visualizations.

- **User Interface (Optional)**: Build a user interface within Power BI for an enhanced user experience.

- **Testing the API Endpoint with Postman**: To ensure data accuracy and availability, you can test the API endpoint using Postman.
---

## Prerequisites

Before getting started, ensure you have the following prerequisites:

- **Python 3.x**: Install Python 3.x on your local machine.

- **Required Libraries**: Install the required Python libraries using pip:

  ```shell
  pip install requests pandas
