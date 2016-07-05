import Ember from 'ember';
import LoginRedirect from 'osf-meetings/mixins/login-redirect';

export default Ember.Route.extend(LoginRedirect, {
  model() {
    return this.store.createRecord('conference');
  },
  deactivate: function() {
    var controller = this.get('controller');
    controller.send('killConference');
    controller.set('kill',true);
    controller.set('displayErrors',false);
  },
  actions: {
    back() {
      this.transitionTo('index').then(function(newRoute) {
        newRoute.controller.set('visited', true);
      });
    }
  }
});
