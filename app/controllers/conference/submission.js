import Ember from 'ember';
//import TaggableMixin from 'ember-osf/mixins/taggable-mixin';
//import EmberValidations from 'ember-validations';

export default Ember.Controller.extend(/*TaggableMixin, EmberValidations,*/ {
    toast : Ember.inject.service(),
    _url : 'files',
    resolve : null,
    latestFileName : null,
    dropzoneOptions : {
        uploadMultiple : false,
        method : 'PUT'
    },

    actions : {
        buildUrl() {
            return this.get('_url');
        },
        preUpload(comp, drop, file) {
            console.log(comp + drop + file);
            return new Ember.RSVP.Promise(resolve => {
                this.set('resolve', resolve);
            });
        },
        success(ignore, dropzone, file, response) {
            console.log(ignore + dropzone + file + response);
        },
        error(ignore, err) {
            console.log(err);
        },
    }
//    displayErrors: false,
//    tagError: false,
//    kill: true,
//
//    validations: {
//        'model.title': {
//            length: {minimum: 3, maximum: 200, messages: {
//                tooShort: 'Please enter a valid title',
//                tooLong: 'Title exceeds limit of 200 characters'
//            }}
//        },
//        //TODO: Validation for contributors?
//        'model.description': {
//            length: {minimum: 6, maximum: 2000, messages: {
//                tooShort: 'Please enter a valid description',
//                tooLong: 'Description exceeds limit of 2000 characters.'
//            }}
//        }
//    },
//
//    actions: {
//        killSubmission() {
//            if (this.get('kill')) {
//                this.get('model').destroyRecord();
//            }
//        },
//        saveNodeSubmission(newNode, id) {
//            if (this.get('isValid')) {
//                this.set('kill',false);
//                newNode.setProperties({
//                    category: 'project',
//                });
//                document.getElementById("fileSubmission").reset();
//                var self = this;
//                newNode.save().then(function() {
//                    self.transitionToRoute('conference.index.index', id);
//                });
//            }
//            else {
//                this.set('displayErrors',true);
//            }
//        }
//    }
});
