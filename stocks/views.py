# 

import csv
import os
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# File path for storing CSV
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'stocks_data.csv')

class StocksListCreateView(APIView):

    def get(self, request, *args, **kwargs):
        # Read the data from the CSV file
        try:
            with open(CSV_FILE_PATH, mode='r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
            return Response(data, status=status.HTTP_200_OK)
        except FileNotFoundError:
            return Response({"message": "No data available"}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Get data from request
        data = request.data

        # Check if the CSV file already exists
        file_exists = os.path.isfile(CSV_FILE_PATH)

        # Write data to the CSV file
        with open(CSV_FILE_PATH, mode='a', newline='') as file:
            fieldnames = ['symbol_type', 'stock_name', 'symbol_name', 'expiry_date', 
                          'strike_price', 'order_type', 'entry_type', 'option_type', 'created_at']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the header if the file is being created for the first time
            if not file_exists:
                writer.writeheader()

            writer.writerow({
                'symbol_type': data.get('symbol_type', ''),
                'stock_name': data.get('stock_name', ''),
                'symbol_name': data.get('symbol_name', ''),
                'expiry_date': data.get('expiry_date', ''),
                'strike_price': data.get('strike_price', ''),
                'order_type': data.get('order_type', ''),
                'entry_type': data.get('entry_type', ''),
                'option_type': data.get('option_type', ''),
                'created_at': data.get('created_at', '')  # Consider using current time if needed
            })

        return JsonResponse({"message": "Data saved to CSV successfully"}, status=status.HTTP_201_CREATED)
