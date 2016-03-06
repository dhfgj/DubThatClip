function uploadVoiceTrack(evt) {
	evt.preventDefault();

	var voiceTrackId =  {"voiceTrackId": //get voice id

	//send info to server
	$.post("/getvoiceover", voiceTrackId, function (result) {
		// do something when we get a response back.
	}
}