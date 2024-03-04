import re

def extract_state(location):
    state_pattern = r',\s*([A-Z]{2})|\b(?:Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New\s+Hampshire|New\s+Jersey|New\s+Mexico|New\s+York|North\s+Carolina|North\s+Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode\s+Island|South\s+Carolina|South\s+Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West\s+Virginia|Wisconsin|Wyoming)\b'
    match = re.search(state_pattern, location)
    if match:   
        if match.group().startswith(", "):
            return match.group()[2:]
        return match.group()         
    else:
        return "Remote"

job_locations = [
    "Arlington, Virginia, United States (Hybrid)",
    "Las Vegas, NV (On-site)",
    "United States (Remote)",
    "College Park, MD (On-site)",
    "Shreveport, LA (On-site)",
    "San Jose, CA",
    "San Jose, CA",
    "San Jose, CA",
    "Overland Park, KS (On-site)",
    "New York, NY (Hybrid)",
    "Omaha, NE (On-site)",
    "United States (Remote)",
    "Auburn Hills, MI (On-site)",
    "San Jose, CA",
    "New York, NY (On-site)",
    "Schaumburg, IL (Hybrid)",
    "San Diego, CA",
    "Cambridge, MA (Remote)",
    "United States (Remote)",
    "Santa Ana, CA",
    "Herndon, VA",
    "College Station, TX",
    "Spring House, PA (Hybrid)",
    "Atlanta, GA (On-site)",
    "Morristown, NJ (On-site)",
    "Louisville, KY (On-site)",
    "Greensboro, NC (On-site)",
    "Grand Prairie, TX (On-site)",
    "Alexandria, VA (On-site)",
    "United States (Remote)",
    "San Jose, CA"
]

for location in job_locations:
    state = extract_state(location)
    print(state)
