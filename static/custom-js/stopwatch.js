function Stopwatch(elem, counter) {
	this.timesReset = 3;
	this.timeForPopup = 30;
	this.dismissPressed = false;
	var time = 0;
	var offset;
	var interval;

	function checkForDismiss() {
		setTimeout(function() {
			if (!this.dismissPressed) {
				this.dismissPressed = true;
				this.reset;
				if (!this.isOn) {
					this.start();
					$('#start-btn').innerHTML = 'Stop';
				}
			}
		}, 300);
	}

	function update() {
		let convertedPopupTime = 60 * 1000 * this.timeForPopup;
		if (this.isOn) {
			time += delta();

			if (time >= convertedPopupTime) {
				// 10 minutes
				const timeout = 3600000;

				//  launch the model
				$('#launchModal').trigger('click');
				toggleStart(this);
				setTimeout(function() {
					if (!this.dismissPressed) {
						callHelp();
						elem.textContent = 'The system is calling for help!';
						$('#dismissBtn').trigger('click');
					}
				}, timeout);
			}
		}

		elem.textContent = timeFormatter(time);
	}

	function delta() {
		var now = Date.now();
		var timePassed = now - offset;

		offset = now;

		return timePassed;
	}

	function timeFormatter(time) {
		time = new Date(time);
		var minutes = time.getMinutes().toString();
		var seconds = time.getSeconds().toString();
		var milliseconds = time.getMilliseconds().toString();

		if (minutes.length < 2) {
			minutes = '0' + minutes;
		}

		if (seconds.length < 2) {
			seconds = '0' + seconds;
		}

		while (milliseconds.length < 3) {
			milliseconds = '0' + milliseconds;
		}

		return 'Time: ' + minutes + ' : ' + seconds + ' . ' + milliseconds;
	}

	this.setPopupTime = function(newPopupTime) {
		this.timeForPopup = newPopupTime;
	};

	this.start = function() {
		if (!this.dismissPressed) {
			interval = setInterval(update.bind(this), 10);
			offset = Date.now();
			this.isOn = true;
		}
	};

	this.stop = function() {
		if (!this.dismissPressed) {
			clearInterval(interval);
			interval = null;
			this.isOn = false;
		}
	};

	this.reset = function() {
		if (!this.dismissPressed) {
			time = 0;
			update();
		}
	};

	this.isOn = false;
}

function toggleStart(watch) {
	if (watch.isOn) {
		watch.stop();
		$('#start-btn').innerHTML = 'Start';
	} else {
		watch.start();
		$('#start-btn').innerHTML = 'Stop';
	}
}

function callHelp() {
	console.log('Called help');
}

$(document).ready(function() {
	// Get the modal
	var counter = document.getElementById('helpCounter');
	let modal = document.getElementById('popupModal');
	let timer = document.getElementById('time-string');
	let btnStart = document.getElementById('start-btn');
	let btnReset = document.getElementById('reset-btn');

	let watch = new Stopwatch(timer, counter);
	let dismiss = document.getElementById('dismissBtn');
	watch.timeForPopup = 30;

	let chosenTime = document.getElementById('chosen-time');
	let radio1 = document.getElementById('15m');
	let radio2 = document.getElementById('30m');
	let radio3 = document.getElementById('60m');

	radio1.addEventListener('click', function() {
		watch.setPopupTime(15);
		chosenTime.innerHTML = '15 minutes';
	});

	radio2.addEventListener('click', function() {
		watch.setPopupTime(30);
		chosenTime.innerHTML = '30 minutes';
	});
	radio3.addEventListener('click', function() {
		watch.setPopupTime(60);
		chosenTime.innerHTML = '1 hours';
	});

	btnStart.addEventListener('click', function() {
		if (!watch.dismissPressed) {
			if (watch.isOn) {
				watch.stop();
				btnStart.innerHTML = 'Start';
			} else {
				watch.start();
				btnStart.innerHTML = 'Stop';
			}
		}
	});

	btnReset.addEventListener('click', function() {
		if (!watch.dismissPressed) {
			watch.reset();
		}
	});

	$('close')[0].click(() => {
		watch.dismissPressed = true;
	});

	dismiss.addEventListener('click', function() {
		console.log('dismiss button clicked');
		watch.dismissPressed = true;
	});
	window.onclick = function(event) {
		if (event.target == modal) {
			console.log('modal click');
			watch.dismissPressed = true;
			// setTimeout(function() {
			// 	$('#start-btn').trigger('click');
			// 	watch.reset;
			// }, 300);
		}
	};
});
