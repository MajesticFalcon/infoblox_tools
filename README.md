---

# Infoblox Management Tools

This project contains a Python interface for managing various aspects of Infoblox, including DHCP pool usage. The `Infoblox` class in the Python script provides a way to interface with Infoblox's API and perform common management tasks in a scalable, object-oriented way.

## Usage

To use the Infoblox management tools, you will need to import the `Infoblox` class from the Python script and create an instance with your Infoblox's URL, username, and password.

```python
from infoblox import Infoblox

infoblox = Infoblox(url="https://your-infoblox-url", username="your-username", password="your-password")
```

## Features

Currently, the `Infoblox` class supports several methods for managing DHCP:

- `get_dhcp_scopes()`: Retrieves all DHCP scopes.
- `get_dhcp_pools(scope)`: Retrieves all DHCP pools within a specific scope.
- `get_pool_usage(pool)`: Retrieves usage information for a specific pool.
- `print_high_usage_pools()`: Prints out information about pools with high usage (>90%).

The class can be easily extended to include more methods for managing other aspects of Infoblox.

## Future Work

The aim of this project is to provide a comprehensive set of tools for managing Infoblox. We plan to extend the `Infoblox` class with more methods for managing other aspects of Infoblox, such as DNS records, IPAM, and more.

## Contributing

We welcome contributions to this project! Please feel free to submit pull requests with additional methods for the `Infoblox` class or enhancements to existing methods.

---
