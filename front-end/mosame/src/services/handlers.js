export function displayError(toaster, error) {
    setTimeout(() => {
        toaster.error(error, {
            max: 1,
            position: "top",
            duration: 2000
        });
    }, "200");
}

export function displaySuccess(toaster, message) {
    setTimeout(() => {
        toaster.success(message, {
            max: 1,
            position: "top",
            duration: 2000
        });
    }, "200");
}

export default {displayError, displaySuccess};