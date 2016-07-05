import Ember from 'ember';
import LoginRedirectMixin from 'osf-meetings/mixins/login-redirect';
import { module, test } from 'qunit';

module('Unit | Mixin | login redirect');

// Replace this with your real tests.
test('it works', function(assert) {
  let LoginRedirectObject = Ember.Object.extend(LoginRedirectMixin);
  let subject = LoginRedirectObject.create();
  assert.ok(subject);
});
