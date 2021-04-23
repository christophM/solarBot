import json

STATUS_FILENAME = "/home/pi/solarBot/status.json"

def read_status():
    with open(STATUS_FILENAME) as json_data_file:
        status = json.load(json_data_file)
    return(status)

def increase(status, what, by):
    status[what] += by 
    return(status)

def write_status(status):
    with open(STATUS_FILENAME, "w") as outfile:
        outfile.write(json.dumps(status))

def main():
    status = read_status()
    status = increase(status, what = "wakeups", by = 1)
    write_status(status)

if __name__ == "__main__":
    main()

