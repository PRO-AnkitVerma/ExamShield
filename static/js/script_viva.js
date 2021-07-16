const socket = io("https://boiling-scrubland-01865.herokuapp.com/");

console.log(ROOM_ID)
const videoGrid = document.getElementById("video-grid");
const myPeer = new Peer(undefined, {});
// myPeer.host = "localhost";
myPeer.host = "boiling-scrubland-01865";

// myPeer.port = "3001";
// myPeer.path = "/test"

const myVideo = document.createElement("video");
myVideo.muted = true;

const peers = {};

navigator.mediaDevices
    .getUserMedia({
        video: true,
        // audio: true
    })
    .then((stream) => {
        addVideoStream(myVideo, stream);
        console.log("video started from the script viva")
        myPeer.on("call", (call) => {
            call.answer(stream);
            const video = document.createElement("video");
            call.on("stream", (userVideoStream) => {
                addVideoStream(video, userVideoStream);
            });
        });

        socket.on("user-connected", (userId) => {
            connectToNewUser(userId, stream);
        });
    });

socket.on("user-disconnected", (userId) => {
    if (peers[userId]) peers[userId].close();
});

myPeer.on("open", (id) => {
    console.log(id);
    console.log("JOIN event will be published here")
    socket.emit("join-room", ROOM_ID, id);
});

function connectToNewUser(userId, stream) {
    const call = myPeer.call(userId, stream);
    const video = document.createElement("video");
    call.on("stream", (userVideoStream) => {
        addVideoStream(video, userVideoStream);
    });
    call.on("close", () => {
        video.remove();
    });
    peers[userId] = call;
}

function addVideoStream(video, stream) {
    video.srcObject = stream;
    video.addEventListener("loadedmetadata", () => {
        video.play();
    });
    videoGrid.appendChild(video);
    console.log("=======================================");
    console.log("OK VIDEO APPENED SUCCESSFULLY");
    console.log("=======================================");
}


