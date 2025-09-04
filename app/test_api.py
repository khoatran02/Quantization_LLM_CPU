# test_api.py
import requests
import json
import time

BASE = "http://127.0.0.1:8000"

def test_health_endpoint():
    """Test the health endpoint"""
    print("🧪 Testing Health Endpoint")
    print("-" * 40)

    url = f"{BASE}/model/health"
    headers = {
        'accept': 'application/json'
    }
    
    try:
        start_time = time.time()
        response = requests.get(url, headers=headers, timeout=100)
        print(response)
        end_time = time.time()
        
        print(f"URL: {url}")
        print(f"Response time: {end_time - start_time:.2f} seconds")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Health endpoint successful!")
            response_data = response.json()
            print(json.dumps(response_data, indent=2, ensure_ascii=False))
            
            # Check if the expected fields are present
            if 'status' in response_data:
                print(f"📊 Status: {response_data['status']}")
            if 'message' in response_data:
                print(f"💬 Message: {response_data['message']}")
            if 'timestamp' in response_data:
                print(f"⏰ Timestamp: {response_data['timestamp']}")
                
        else:
            print(f"❌ Health endpoint failed with status: {response.status_code}")
            print(f"Response text: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Could not connect to the server.")
        print(f"Make sure the Flask server is running on {BASE}")
        return False
    except requests.exceptions.Timeout:
        print("❌ Request timeout: The server took too long to respond.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Exception: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {e}")
        print(f"Response text: {response.text}")
        return False
    
    print()  # Empty line for spacing
    return response.status_code == 200

def test_generate_response_endpoint():
    """Test the generate response endpoint"""
    print("🧪 Testing Generate Response Endpoint")
    print("-" * 50)

    url = f"{BASE}/model/generate_response"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # Request data
    data = {
        "json_input": {
            "company_name": "ABC",
            "website": "https://www.mvideo.ru",
            "founding_year": 1993,
            "number_of_employees": 30000,
            "industry_sector": "Retail Electronics",
            "headquarters": "Moscow, Russia",
            "estimated_assets_last_3_years": {"2022": 4500000000, "2023": 4800000000, "2024": 5100000000},
            "estimated_expenses_last_3_years": {"2022": 4200000000, "2023": 4400000000, "2024": 4600000000},
            "estimated_profit_last_3_years": {"2022": 120000000, "2023": 150000000, "2024": 180000000},
            "estimated_cashflow_invest_last_3_years": {"2022": -150000000, "2023": -180000000, "2024": -200000000},
            "financial_ratios": {
                "roa": {"2022": 2.7, "2023": 3.1, "2024": 3.5},
                "roe": {"2022": 8.5, "2023": 9.8, "2024": 11.0},
                "debt_to_asset": {"2022": 0.68, "2023": 0.65, "2024": 0.62},
                "debt_to_equity": {"2022": 2.13, "2023": 1.86, "2024": 1.63},
                "ebitda": {"2022": 350000000, "2023": 380000000, "2024": 410000000},
                "pe_ratio": {"2022": 9.8, "2023": 10.5, "2024": 11.2},
                "industry_pe": {"2022": 12.3, "2023": 11.8, "2024": 11.4},
                "net_debt": 50,
                "free_cash_flow": [100, 150, 200, 250, 300],
                "terminal_growth_rate": 0.05,
                "discount_rate": 0.12,
                "shares_outstanding": 20
            },
            "analysis_summary": {
                "valuation": {
                    "level": "REASONABLE",
                    "note": "P/E is 15.0x, compared to industry average of 14.5x.",
                    "enterprise_value": 1500.0,
                    "intrinsic_value_per_share": "125,000 VND",
                    "most_recent_fcff": "150 billion VND",
                    "wacc": "12%",
                    "forecast_growth_rate": "5%",
                    "terminal_growth_rate": "2%",
                    "equity_value": 1450.0,
                    "equity_value_per_share": 145.0,
                    "industry_avg_ev_ebitda": 15.0,
                    "implied_enterprise_value": 1500.0,
                    "implied_equity_value": 1450.0
                },
                "validation": {
                    "validation_summary": {
                        "all_methods_consistent": True,
                        "valuation_range_per_share": "120 - 130",
                        "recommended_fair_value": 125,
                        "confidence_level": "High",
                        "notes": "DCF and multiples are consistent within ±5%"
                    }
                }
            }
        },
        "model_type": "4bit",
        "max_tokens": 1000
    }
    
    try:
        print(f"URL: {url}")
        print("Sending request... (this may take a while)")
        
        start_time = time.time()
        response = requests.post(url, headers=headers, json=data, timeout=10000)
        end_time = time.time()
        
        print(f"Response time: {end_time - start_time:.2f} seconds")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Generate response successful!")
            
            response_data = response.json()
            print("\n📋 Full Response:")
            print(json.dumps(response_data, indent=2, ensure_ascii=False))
            
            # Extract and display key information
            if 'response' in response_data:
                print(f"\n🤖 AI Response:")
                print(response_data['response'])
                
            if 'model_used' in response_data:
                print(f"\n🔧 Model Used: {response_data['model_used']}")
                
            if 'tokens_used' in response_data:
                print(f"📊 Tokens Used: {response_data['tokens_used']}")
                
            if 'error' in response_data:
                print(f"\n❌ Error: {response_data['error']}")
                
        else:
            print(f"❌ Generate response failed with status: {response.status_code}")
            print(f"Response text: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Could not connect to the server.")
    except requests.exceptions.Timeout:
        print("❌ Request timeout: The server took too long to respond.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Exception: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {e}")
        print(f"Response text: {response.text}")

def test_server_status():
    """Test basic server status"""
    print("🌐 Testing Server Status")
    print("-" * 30)
    
    try:
        response = requests.get(f"{BASE}/", timeout=5)
        print(f"Root endpoint - Status: {response.status_code}")
        print(f"Root endpoint - Response: {response.text[:100]}...")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the Flask server first.")
        return False
    except Exception as e:
        print(f"❌ Error checking server status: {e}")
        return False
    
    print()  # Empty line for spacing
    return True

if __name__ == "__main__":
    print("🚀 Starting API Tests")
    print("=" * 60)
    
    # Test basic server status first
    server_running = test_server_status()
    
    if server_running:
        # Test health endpoint
        health_ok = test_health_endpoint()
        # Only test generate response if health is OK
        if health_ok:
            test_generate_response_endpoint()
        else:
            print("❌ Skipping generate response test due to health check failure")
    else:
        print("❌ Cannot run tests - server is not available")
    
    print("\n" + "=" * 60)
    print("🏁 Testing completed")