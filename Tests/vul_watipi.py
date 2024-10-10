import subprocess
import json

# The target URL to scan
# url = "http://google.com"
def vulnerabilityFinder(domain):
    res = {}
    # Command to execute Wapiti with JSON output
    command = [
        "wapiti",           # Call the wapiti command
        "-u", domain,          # Target URL
        "-f", "json",       # Output format as JSON
        "-o", "report.json" # Save the report to report.json
    ]

    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)


        # Open the generated JSON report and parse it
        with open("report.json", "r") as json_file:
            report_data = json.load(json_file)


        # vulnerabilities = json.dumps(report_data["vulnerabilities"])
        vulnerabilities = report_data["vulnerabilities"]
        
        for vul in vulnerabilities:
            if vulnerabilities[vul]:
                # print(vulnerabilities[vul])
                res.update({str(vul) : json.dumps(vulnerabilities[vul])})

    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except FileNotFoundError:
        print("Error: Report file not found.")
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON report.")
    finally:
        return res
    
    
print(vulnerabilityFinder("http://facebook.com"))