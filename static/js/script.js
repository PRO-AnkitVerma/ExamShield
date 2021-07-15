const socket = io("https://boiling-scrubland-01865.herokuapp.com/");
console.log(ROOM_ID)
const videoGrid = document.getElementById("video-grid");
const myPeer = new Peer(undefined, {});
myPeer.host = "boiling-scrubland-01865";
// myPeer.port = "3001";
// myPeer.path = "/test"

const myVideo = document.createElement("video");
let counter = 1;
myVideo.muted = true;

navigator.mediaDevices
    .getUserMedia({
        video: true,
        // audio: true
    })
    .then((stream) => {
        addVideoStream(myVideo, stream);

        //TODO: add face detection here!
        myPeer.on('call', call => {
            call.answer(stream);
            const video = document.createElement('video');
            call.on('stream', userVideoStream => {
                addVideoStream(video, userVideoStream);
                //console.log('ok');
            });
        });

        socket.on("user-connected", (userId) => {
            console.log("Connection is being called")
            connectToNewUser(userId, stream);
        });
    });

myPeer.on("open", (id) => {
    console.log(id);
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
}

function addVideoStream(video, stream) {
    if (counter === 2) {
        video.srcObject = stream;
        video.addEventListener("loadedmetadata", () => {
            video.play();
        });
        videoGrid.appendChild(video);
    }
    ++counter;
}
