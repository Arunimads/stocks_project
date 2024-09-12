import csv
import os
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from stocks.order_fire import send_transaction  # Ensure this import is correct

# File path for storing CSV
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'stocks_data.csv')

class StocksListCreateView(APIView):

    def get(self, request, *args, **kwargs):
        """Fetch data from CSV file and return it."""
        try:
            with open(CSV_FILE_PATH, mode='r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                print(f"Data fetched: {data}")  # Log data fetched
            return Response(data, status=status.HTTP_200_OK)
        except FileNotFoundError:
            return Response({"message": "No data available"}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Save data to CSV and call send_transaction with the received data."""
        data = request.data
        print(f"Received data: {data}")  # Log the received data

        # Check if all required fields are present and validate their types
        required_fields = {
            'symbol_type': str,
            'stock_name': str,
            'symbol_name': str,
            'expiry_date': str,
            'strike_price': str,
            'order_type': str,
            'entry_type': str,
            'option_type': str,
            'price_limit': str,
            'quantity': str
        }
        
        missing_fields = [field for field, field_type in required_fields.items() if field not in data or not isinstance(data.get(field), field_type)]
        
        if missing_fields:
            return JsonResponse({"message": f"Missing or invalid fields: {missing_fields}"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the CSV file already exists
        file_exists = os.path.isfile(CSV_FILE_PATH)

        # Write data to the CSV file
        try:
            with open(CSV_FILE_PATH, mode='a', newline='') as file:
                fieldnames = ['symbol_type', 'stock_name', 'symbol_name', 'expiry_date', 
                              'strike_price', 'order_type', 'entry_type', 'option_type', 
                              'price_limit', 'quantity']
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
                    'price_limit': data.get('price_limit', ''),
                    'quantity': data.get('quantity', ''),
                })
                print(f"Data saved to CSV: {data.get('symbol_name')}")

        except Exception as e:
            print(f"Error writing to CSV: {e}")
            return JsonResponse({"message": "Failed to save data to CSV"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Call send_transaction with the data received from the frontend
        try:
            print(f"Attempting to call send_transaction with: {data}")  # Log before calling the function
            # send_transaction(
            #     data.get('order_type'),       
            #    data.get('stock_name'),       
            #     data.get('symbol_name'),     
            #     data.get('expiry_date'),     
            #     data.get('strike_price'),   
            #    data.get('entry_type'),       
            #     data.get('option_type') ,
            #     data.get('quantity') ,
                     
            # )
            print("Transaction sent successfully!")
        except Exception as e:
            print(f"Error in send_transaction: {e}")
            return JsonResponse({"message": f"Failed to send transaction: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({"message": "Data saved to CSV and transaction sent successfully"}, status=status.HTTP_201_CREATED)
