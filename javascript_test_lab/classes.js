class Materializer {
    constructor(target, activated = false){
        this.target = target;
        this.activated = activated;
    }
    activate() {
        return this.activated = true;
    }
    materialize() {
        if (this.activated == true) {
            return this.target;
        } else {
            return undefined;
        }
    }
}

/* TEST CASES 
// The following lines of code are not required for the solution, but can be
// used by you to test your solution.
const m = new Materializer('Kevin');

console.log(m.materialize()); // would return undefined

console.log(m.activated); // would print "false"

m.activate();
console.log(m.activated); // would print "true"

console.log(m.materialize()); // would print "Kevin"
*/