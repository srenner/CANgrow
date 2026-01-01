# System Architecture

AI Prompt:

```plaintext
Generate a Mermaid architecture diagram for the following system:

- Main server running on a Raspberry Pi 5 with PiCAN hat
	- FastAPI defines the database structure and handles data interaction with the web app
	- SQLite database stores the data
	- Vue.js app is the primary user interface for the system
	- A Python service sends and receives CAN bus messages to and from the nodes
		- The Python service sends select CAN messages to a FastAPI endpoint to be served to the UI via WebSockets
		- The Python service also saves some CAN messages to SQLite directly
- 1 or more System Nodes running on a microcontroller with a CAN bus controller
	- Sends and receives CAN bus messages to and from the main server
```

Claude Sonnet 4.5 output:

```mermaid
graph TB
    subgraph RPi["Raspberry Pi 5 + PiCAN Hat"]
        VueApp["Vue.js Web App<br/>(User Interface)"]
        FastAPI["FastAPI Server<br/>(REST API & DB Schema)"]
        SQLite["SQLite Database<br/>(Data Storage)"]
        CANService["Python CAN Service<br/>(CAN Message Handler)"]
        CANHat["PiCAN Hat<br/>(CAN Controller)"]
    end
    
    subgraph CANBus["CAN Bus Network"]
        Bus["CAN Bus"]
    end
    
    subgraph Nodes["System Nodes"]
        Node1["Microcontroller Node 1<br/>(CAN Controller)"]
        Node2["Microcontroller Node 2<br/>(CAN Controller)"]
        NodeN["Microcontroller Node N<br/>(CAN Controller)"]
    end
    
    VueApp <-->|HTTP/REST| FastAPI
    VueApp -.->|WebSocket Real-time Data| FastAPI
    FastAPI <-->|SQL Queries| SQLite
    CANService -->|POST Select Messages| FastAPI
    CANService -->|Save CAN Messages| SQLite
    CANService <-->|CAN Messages| CANHat
    
    CANHat <-->|CAN Protocol| Bus
    Bus <-->|CAN Protocol| Node1
    Bus <-->|CAN Protocol| Node2
    Bus <-->|CAN Protocol| NodeN
    
    style RPi fill:#e1f5e1
    style CANBus fill:#e3f2fd
    style Nodes fill:#fff3e0
```
