import {TestBed} from '@angular/core/testing';
import {setupTestModule} from '../test/test.module.spec';
import {MarkdownServiceService} from './markdown-service.service';


describe('MarkdownServiceService', () => {
  let service: MarkdownServiceService;

  beforeEach(() => {
    setupTestModule();
    service = TestBed.inject(MarkdownServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
