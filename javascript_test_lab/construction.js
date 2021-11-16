function construct(name) {
    const matter_initatiator = {
        name: name,
        material: 'human',
        assemble: true,
        duration: 1000
    };
    return matter_initatiator;
}

/* TEST CASE
const somePerson = construct('Kevin');
console.log('name is: ' + somePerson.name); // should be "Kevin"
console.log('duration is: ' + somePerson.duration); // should be 1000
*/