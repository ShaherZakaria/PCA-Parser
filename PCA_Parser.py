import os
import csv
from datetime import datetime

def parse_file_info(file_path, output_csv):
    parsed_data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if '|' not in line:
                    continue  # Skip invalid lines
                file_to_parse= os.path.basename(file_path)
                #print(file_to_parse)
                
                if file_to_parse == "PcaAppLaunchDic.txt":
                
                    split=line.split('|')
                
                    file_pathValue= split[0] 
                    last_execution = split[1]
                    
                    # Extract file name
                    file_name = os.path.basename(file_pathValue)
                    
                    # Extract directory
                    directory = os.path.dirname(file_pathValue)
                    
                    # Convert last_execution to a datetime object
                    last_execution = datetime.strptime(last_execution.strip(), "%Y-%m-%d %H:%M:%S.%f")
                    
                    parsed_data.append([file_name, directory, last_execution])
                    
                else:
                
                    Runtime, Run_status, Executable_path, Description, Vendor, Version, APPID, Exitcode = line.split('|')
                    #print (Runtime)
                    
                    # Extract file name
                    file_name = os.path.basename(Executable_path)
                    
                    # Extract directory
                    directory = os.path.dirname(Executable_path)
                    
                    # Convert last_execution to a datetime object
                    #Runtime = datetime.strptime(Runtime.strip(), "%Y-%m-%d %H:%M:%S.%f")
                    
                    parsed_data.append([file_name, directory, Runtime, Run_status, Description, Vendor, Version, APPID,Exitcode])
        
        # Write output to CSV file
        with open(output_csv, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            
            csv_writer.writerows(parsed_data)
        
        return f"Data written to {output_csv}"

    except (ValueError, FileNotFoundError) as e:
        return {"Error": f"Failed to parse file info: {e}"}

# Example usage
file_path = [r"PcaAppLaunchDic.txt",r"PcaGeneralDb0.txt",r"PcaGeneralDb1.txt"]
output_csv = ["parsed_PcaAppLaunchDic.csv","parsed_PcaGeneralDbx.csv"]


for file in file_path:
    file_to_parse= os.path.basename(file)           
    if file_to_parse == "PcaAppLaunchDic.txt":
        with open(output_csv[0], 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            #csv_writer.writerow(["file_name", "directory", "Runtime", "Run_status", "Description", "Vendor", "Version", "APPID","Exitcode"])
            csv_writer.writerow(["File Name", "Directory", "Last Execution"])
        result = parse_file_info(file, output_csv[0])
    elif file_to_parse=="PcaGeneralDb0.txt":
        with open(output_csv[1], 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["file_name", "directory", "Runtime", "Run_status", "Description", "Vendor", "Version", "APPID","Exitcode"])
            #csv_writer.writerow(["File Name", "Directory", "Last Execution"])
        result = parse_file_info(file, output_csv[1])
        
    else:
        print ("the third file")
        result = parse_file_info(file, output_csv[1])
        

    

print(result)
