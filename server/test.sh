#!/bin/bash

HOST=http://127.0.0.1:8000

# POST location - Should be 200
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"device_id":"123","location":"ICU"}' \
    $HOST/location

echo

# POST location - Should be 200
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"device_id":"456","location":"Room 300"}' \
  $HOST/location

echo


# GET location - Should be 200
curl --header "Content-Type: application/json" \
  --request GET \
  $HOST/location

echo

# POST power status - Should be 200
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"device_id":"123","status":true}' \
  $HOST/power

echo


# POST power status - Should be 200
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"device_id":"456","status":false}' \
  $HOST/power

echo


# GET location - Should be 200
curl --header "Content-Type: application/json" \
  --request GET \
  $HOST/power

echo
