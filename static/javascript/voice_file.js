function uploadVoiceTrack(evt) {
	evt.preventDefault();

	var voiceLink = $("#voiceRecorder").contents().find("#idDownloadAsMp3Link").href();

	var idxStart, idxEnd;

	for (var i=0; i<= voiceLink.length; i++){
		if (i === "=") {
			idxStart = i+1;
		}
		if (i === "&") {
			idxEnd = i;
		}
	}

	var voiceTrackId =  {"voiceTrackId": voiceLink.slice(idxStart, idxEnd)}//get voice id

	//send info to server
	$.post("/getvoiceover", voiceTrackId, function (result) {
		// do something when we get a response back.
	}
}