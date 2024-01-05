#!/bin/sh

# Check if the bit.ly URL is provided as a parameter
if [ $# -eq 0 ]; then
  echo "Usage: $0 <bit.ly URL>"
  exit 1
fi

# Get the bit.ly URL from the first parameter
url=$1

# Use curl to fetch the headers of the URL and grep to extract the "Location" header
location=$(curl -s -I "$url" | grep -i "Location" | cut -d' ' -f2-)

# Display the real address
echo $location
