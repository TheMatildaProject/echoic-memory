# Echoic Memory
Echoic memory is one of the sensory memory registers; a component of sensory memory (SM) that is specific to retaining auditory information.

And so, this is a Python app that connects to Spotify and Youtube APIs to seek the songs I want to hear, then saves them on the memory cortex (ElasticSearch) to give me clever suggestions of what to listen next.

## Installation

### Build Image
`docker build . -t echoic-memory`

### Run
`docker run -t --name echoic-memory -p 5006:5000 echoic-memory`
or 
`docker-compose up --force-recreate` (also starts and binds elasticsearch)