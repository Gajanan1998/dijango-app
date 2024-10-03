"use strict";
! function() {
	var t = document.querySelector("#basic-alert"),
		e = document.querySelector("#with-title"),
		n = document.querySelector("#footer-alert"),
		o = document.querySelector("#html-alert"),
		i = document.querySelector("#position-top-start"),
		s = document.querySelector("#position-top-end"),
		c = document.querySelector("#position-bottom-start"),
		a = document.querySelector("#position-bottom-end"),
		l = document.querySelector("#bounce-in-animation"),
		r = document.querySelector("#fade-in-animation"),
		u = document.querySelector("#flip-x-animation"),
		m = document.querySelector("#tada-animation"),
		f = document.querySelector("#shake-animation"),
		w = document.querySelector("#type-success"),
		b = document.querySelector("#type-info"),
		d = document.querySelector("#type-warning"),
		h = document.querySelector("#type-error"),
		y = document.querySelector("#type-question"),
		g = document.querySelector("#custom-image"),
		S = document.querySelector("#auto-close"),
		p = document.querySelector("#outside-click"),
		v = document.querySelector("#progress-steps"),
		B = document.querySelector("#ajax-request"),
		C = document.querySelector("#confirm-text"),
		k = document.querySelector("#confirm-color");
	t && (t.onclick = function() {
		Swal.fire({
			title: "Any fool can use a computer",
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), e && (e.onclick = function() {
		Swal.fire({
			title: "The Internet?,",
			text: "That thing is still around?",
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), n && (n.onclick = function() {
		Swal.fire({
			icon: "error",
			title: "Oops...",
			text: "Something went wrong!",
			footer: "<a href>Why do I have this issue?</a>",
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), o && (o.onclick = function() {
		Swal.fire({
			title: "<strong>HTML <u>example</u></strong>",
			icon: "info",
			html: 'You can use <b>bold text</b>, <a href="https://pixinvent.com/" target="_blank">links</a> and other HTML tags',
			showCloseButton: !0,
			showCancelButton: !0,
			focusConfirm: !1,
			confirmButtonText: '<i class="mdi mdi-thumb-up-outline me-2"></i> Great!',
			confirmButtonAriaLabel: "Thumbs up, great!",
			cancelButtonText: '<i class="mdi mdi-thumb-down-outline"></i>',
			cancelButtonAriaLabel: "Thumbs down",
			customClass: {
				confirmButton: "btn btn-primary me-3 waves-effect waves-light",
				cancelButton: "btn btn-outline-secondary btn-icon waves-effect"
			},
			buttonsStyling: !1
		})
	}), i && (i.onclick = function() {
		Swal.fire({
			position: "top-start",
			icon: "success",
			title: "Your work has been saved",
			showConfirmButton: !1,
			timer: 1500,
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), s && (s.onclick = function() {
		Swal.fire({
			position: "top-end",
			icon: "success",
			title: "Your work has been saved",
			showConfirmButton: !1,
			timer: 1500,
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), c && (c.onclick = function() {
		Swal.fire({
			position: "bottom-start",
			icon: "success",
			title: "Your work has been saved",
			showConfirmButton: !1,
			timer: 1500,
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), a && (a.onclick = function() {
		Swal.fire({
			position: "bottom-end",
			icon: "success",
			title: "Your work has been saved",
			showConfirmButton: !1,
			timer: 1500,
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), l && (l.onclick = function() {
		Swal.fire({
			title: "Bounce In Animation",
			showClass: {
				popup: "animate__animated animate__bounceIn"
			},
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), r && (r.onclick = function() {
		Swal.fire({
			title: "Fade In Animation",
			showClass: {
				popup: "animate__animated animate__fadeIn"
			},
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), u && (u.onclick = function() {
		Swal.fire({
			title: "Flip In Animation",
			showClass: {
				popup: "animate__animated animate__flipInX"
			},
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), m && (m.onclick = function() {
		Swal.fire({
			title: "Tada Animation",
			showClass: {
				popup: "animate__animated animate__tada"
			},
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), f && (f.onclick = function() {
		Swal.fire({
			title: "Shake Animation",
			showClass: {
				popup: "animate__animated animate__shakeX"
			},
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), w && (w.onclick = function() {
		Swal.fire({
			title: "Issuer Created Successfully!!!",
			//text: "You clicked the button!",
			icon: "success",
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), b && (b.onclick = function() {
		Swal.fire({
			title: "Info!",
			text: "You clicked the button!",
			icon: "info",
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), d && (d.onclick = function() {
		Swal.fire({
			title: "Warning!",
			text: " You clicked the button!",
			icon: "warning",
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), h && (h.onclick = function() {
		Swal.fire({
			title: "Error!",
			text: " You clicked the button!",
			icon: "error",
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), y && (y.onclick = function() {
		Swal.fire({
			title: "Question!",
			text: " You clicked the button!",
			icon: "question",
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), g && (g.onclick = function() {
		Swal.fire({
			title: "Sweet!",
			text: "Modal with a custom image.",
			imageUrl: assetsPath + "img/backgrounds/15.jpg",
			imageWidth: 400,
			imageAlt: "Custom image",
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), S && (S.onclick = function() {
		var t;
		Swal.fire({
			title: "Auto close alert!",
			html: "I will close in <strong></strong> seconds.",
			timer: 2e3,
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1,
			willOpen: function() {
				Swal.showLoading(), t = setInterval(function() {
					Swal.getHtmlContainer().querySelector("strong").textContent = Swal.getTimerLeft()
				}, 100)
			},
			willClose: function() {
				clearInterval(t)
			}
		}).then(function(t) {
			t.dismiss === Swal.DismissReason.timer && console.log("I was closed by the timer")
		})
	}), p && (p.onclick = function() {
		Swal.fire({
			title: "Click outside to close!",
			text: "This is a cool message!",
			backdrop: !0,
			allowOutsideClick: !0,
			customClass: {
				confirmButton: "btn btn-primary waves-effect waves-light"
			},
			buttonsStyling: !1
		})
	}), v && (v.onclick = function() {
		const o = ["1", "2", "3"],
			i = Swal.mixin({
				confirmButtonText: "Forward",
				cancelButtonText: "Back",
				progressSteps: o,
				input: "text",
				inputAttributes: {
					required: !0
				},
				validationMessage: "This field is required"
			});
		!async function() {
			var t = [];
			let e;
			for (e = 0; e < o.length;) {
				var n = await new i({
					title: "Question " + o[e],
					showCancelButton: 0 < e,
					currentProgressStep: e,
					customClass: {
						confirmButton: "btn btn-primary waves-effect waves-light",
						cancelButton: "btn btn-outline-danger waves-effect",
						denyButton: "btn btn-outline-secondary waves-effect"
					}
				});
				n.value ? (t[e] = n.value, e++) : "cancel" === n.dismiss && e--
			}
			Swal.fire(JSON.stringify(t))
		}()
	}), B && (B.onclick = function() {
		Swal.fire({
			title: "Submit your Github username",
			input: "text",
			inputAttributes: {
				autocapitalize: "off"
			},
			showCancelButton: !0,
			confirmButtonText: "Look up",
			showLoaderOnConfirm: !0,
			customClass: {
				confirmButton: "btn btn-primary me-3 waves-effect waves-light",
				cancelButton: "btn btn-outline-danger waves-effect"
			},
			preConfirm: t => fetch("//api.github.com/users/" + t).then(t => {
				if (t.ok) return t.json();
				throw new Error(t.statusText)
			}).catch(t => {
				Swal.showValidationMessage("Request failed:" + t)
			}),
			backdrop: !0,
			allowOutsideClick: () => !Swal.isLoading()
		}).then(t => {
			t.isConfirmed && Swal.fire({
				title: t.value.login + "'s avatar",
				imageUrl: t.value.avatar_url,
				customClass: {
					confirmButtonText: "Close me!",
					confirmButton: "btn btn-primary waves-effect waves-light"
				}
			})
		})
	}), C && (C.onclick = function() {
		Swal.fire({
			title: "Are you sure?",
			text: "You won't be able to revert this!",
			icon: "warning",
			showCancelButton: !0,
			confirmButtonText: "Yes, delete it!",
			customClass: {
				confirmButton: "btn btn-primary me-3 waves-effect waves-light",
				cancelButton: "btn btn-outline-secondary waves-effect"
			},
			buttonsStyling: !1
		}).then(function(t) {
			t.value && Swal.fire({
				icon: "success",
				title: "Deleted!",
				text: "Your file has been deleted.",
				customClass: {
					confirmButton: "btn btn-success waves-effect"
				}
			})
		})
	}), k && (k.onclick = function() {
		Swal.fire({
			title: "Are you sure?",
			text: "You won't be able to revert this!",
			icon: "warning",
			showCancelButton: !0,
			confirmButtonText: "Yes, delete it!",
			customClass: {
				confirmButton: "btn btn-primary me-3 waves-effect waves-light",
				cancelButton: "btn btn-outline-secondary waves-effect"
			},
			buttonsStyling: !1
		}).then(function(t) {
			t.value ? Swal.fire({
				icon: "success",
				title: "Deleted!",
				text: "Your file has been deleted.",
				customClass: {
					confirmButton: "btn btn-success waves-effect"
				}
			}) : t.dismiss === Swal.DismissReason.cancel && Swal.fire({
				title: "Cancelled",
				text: "Your imaginary file is safe :)",
				icon: "error",
				customClass: {
					confirmButton: "btn btn-success waves-effect"
				}
			})
		})
	})
}();