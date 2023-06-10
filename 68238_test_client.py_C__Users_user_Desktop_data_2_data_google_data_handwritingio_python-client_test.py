import pytest

import handwritingio


def test_list_handwritings(client):
  hws = client.list_handwritings()
  assert hws


def test_list_handwriting_limit(client):
  hws = client.list_handwritings({'limit': 1})
  assert len(hws) == 1


def test_list_handwritings_validation(client):
  with pytest.raises(handwritingio.ValidationError) as exc_info:
    client.list_handwritings({'order_by': 'rating_friendliness'})
  # The exception should at least say what field has the problem:
  assert 'order_by' in repr(exc_info.value)


def test_get_handwriting(client, test_handwriting):
  hw = client.get_handwriting(test_handwriting['id'])
  assert hw == test_handwriting


def test_get_handwriting_not_found(client):
  with pytest.raises(handwritingio.APIError) as exc_info:
    client.get_handwriting('made_up_id')
  assert 'not found' in repr(exc_info.value)


def test_render_png(client, test_handwriting):
  image = client.render_png({
      'handwriting_id': test_handwriting['id'],
      'text': 'Hello world!',
  })
  assert image
  assert isinstance(image, bytes)


def test_render_png_missing_text(client, test_handwriting):
  with pytest.raises(handwritingio.ValidationError) as exc_info:
    client.render_png({
        'handwriting_id': test_handwriting['id'],
        # missing text
    })
  assert 'text' in repr(exc_info.value)


def test_render_png_made_up_hw(client):
  with pytest.raises(handwritingio.ValidationError) as exc_info:
    client.render_png({
        'handwriting_id': 'made_up_id',
        'text': 'foo',
    })
  assert 'handwriting_id' in repr(exc_info.value)


def test_render_png_param_validation(client, test_handwriting):
  with pytest.raises(handwritingio.ValidationError) as exc_info:
    client.render_png({
        'handwriting_id': test_handwriting['id'],
        'text': 'trying to make a CMYK PNG',
        'handwriting_color': '(0, 0.1, 0.1, 0.8)',
    })
  assert 'handwriting_color' in repr(exc_info.value)


def test_render_png_multiple_errors(client):
  with pytest.raises(handwritingio.ValidationError) as exc_info:
    client.render_png({
        # missing text and handwriting_id
    })
  assert exc_info.value.errors
  assert len(exc_info.value.errors) == 2


def test_render_pdf(client, test_handwriting):
  image = client.render_pdf({
      'handwriting_id': test_handwriting['id'],
      'text': 'Hello world!',
  })
  assert image
  assert isinstance(image, bytes)


def test_bad_auth(client):
  # Change the credentials:
  client.session.auth = ('foo', 'bar')
  with pytest.raises(handwritingio.AuthorizationError):
    client.list_handwritings()
